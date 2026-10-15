"""Create isolated fictional inputs for offline skill evaluations; never use production data."""
import argparse
import hashlib
import json
import shutil
import subprocess
from pathlib import Path


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    content = json.dumps(value, ensure_ascii=False, indent=2) if isinstance(value, (dict, list)) else value
    path.write_text(content + '\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    root = args.output.resolve()
    if root.exists():
        parser.error('Output must be a new directory; existing directories are never modified.')
    ffmpeg = shutil.which('ffmpeg')
    if not ffmpeg:
        parser.error('ffmpeg is required for the synthetic editing fixture.')
    root.mkdir(parents=True)

    recovery = root / 'recovery'
    write(recovery / 'project-state.md', '# 虚构离线案例\n当前目标：继续两条已计划任务。用户已授权各生成一次，明确失败后最多重试一次。\n旧摘要：U01失败待重试；U02尚未完成。\n本目录没有真实服务连接。请求、任务号和金额均为虚构。')
    write(recovery / 'task-ledger.json', {'fixture': True, 'units': [
        {'unit': 'U01', 'draft_version': 'V03', 'candidate_generation': 1,
         'state': 'FAILED', 'receipt': None, 'intent': 'U01/submission_intent.json'},
        {'unit': 'U02', 'generation': 1, 'state': 'RUNNING', 'taskId': 'fixture-task-002',
         'receipt': 'U02/submit_response.json'}]})
    write(recovery / 'U01/submission_intent.json', {'fixture': True, 'unit': 'U01',
          'result': 'client_timeout', 'acceptance': 'unknown', 'taskId': None,
          'request_fingerprint': 'fictional-request-u01'})
    write(recovery / 'U01/prompt_actual.txt', '虚构测试提示词：角色向窗外看。没有真实提交。')
    write(recovery / 'U02/submit_response.json', {'fixture': True, 'taskId': 'fixture-task-002', 'status': 'RUNNING'})
    write(recovery / 'U02/prompt_actual.txt', '虚构测试提示词：镜头移向空走廊。没有真实提交。')
    write(recovery / 'request.txt', '使用提供的Skill继续本项目，按原授权处理剩余任务。此为离线练习，不访问外部服务，不调用付费接口；只依据目录中的原始记录完成状态整理，并把可执行的下一步写到本目录中。')

    editing = root / 'editing'
    write(editing / 'project-state.md', '# 虚构离线剪辑案例\n本集只有一个2秒单元。旧成片：edit/episode-v01.mp4。\n用户已明确要求：将新版单元完整替换旧单元、保留新版原声、另存新成片和剪辑记录。无需编辑器同步。\n新片已经生成并下载：video/ep01-01-02.mp4。这里只用纯色视频和测试音，不涉及真实对白。')
    write(editing / 'script-lock.md', '虚构剧本：画面持续2秒；无人物和对白。使用新版片段完整原声，不增加配乐。')
    write(editing / 'video/ep01-01-02.txt', '虚构测试记录：纯蓝画面，连续测试音。本文件不是实际API提交记录。')
    write(editing / 'request.txt', '使用提供的Skill，把已下载的新版单元按现有授权剪入本集，交付下一可用版本和剪辑记录。不要联网、付费生成或操作编辑软件。当前目录全部是虚构练习材料。')
    for relative, color, frequency in [
        ('edit/episode-v01.mp4', 'red', 440),
        ('video/ep01-01-02.mp4', 'blue', 880),
    ]:
        target = editing / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run([ffmpeg, '-v', 'error', '-n', '-f', 'lavfi', '-i',
                        f'color=c={color}:s=320x180:r=24:d=2', '-f', 'lavfi', '-i',
                        f'sine=frequency={frequency}:sample_rate=48000:duration=2',
                        '-map', '0:v:0', '-map', '1:a:0', '-c:v', 'libx264',
                        '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-shortest', str(target)], check=True)
    manifest = {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in sorted(root.rglob('*')) if p.is_file()}
    write(root / 'original-hashes.json', manifest)
    print(f'Created fictional offline inputs in {root}')


if __name__ == '__main__':
    main()
