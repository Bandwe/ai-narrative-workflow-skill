# AI Narrative Workflow Skill

面向 AI 短剧和连续叙事视频的通用制作 Skill。让新窗口根据当前文件继续工作，保持剧本、人物、连续性和真实任务记录之间的对应。

适用于已有剧本的分镜制作、连续镜头生成、任务恢复、局部返修、剪辑和交接。也可以只执行其中一个阶段。

完整方法见[通用制作手册 V03](docs/handbook.md)，具体文件和模板见[文件总表](skills/ai-narrative-workflow/references/file-catalog.md)。Release同时提供Skill安装包与独立的手册模板包。

## 它解决什么

- 剧本与逐字对白先锁定，再安排镜头、表演与时长。
- 身份、服装、场景、伤位、道具和参考图槽位分别记录。
- 提交结果不明时恢复原尝试，避免因超时或下载失败重复付费。
- 区分生成成功、用户采用、已剪入、工程同步和完整交付。
- 保留完整对白与原声，定位局部返修范围，标记缺段和未知项。
- 用最少的文件记录把任务交给没有上文记忆的新窗口。

这是方法型 Skill，包含制作经验与模板，不包含视频API客户端或自动剪辑程序。实际工具、服务账号、剧本和素材由每个新项目提供。模型、渠道、规格、价格与授权没有硬编码。

## 文件结构

```text
skills/ai-narrative-workflow/
  SKILL.md                       技能入口与按阶段阅读路径
  agents/openai.yaml              显示信息与调用示例
  references/
    project-state.md             项目状态、文件职责、阶段衔接与工具能力
    storyboard-continuity.md     剧本、资产、表演、镜头与连续性
    generation-recovery.md       提交、查询、下载、重试和批量恢复
    editing-delivery.md          原声、局部返修、剪辑、同步与缺口交付
    file-catalog.md              完整文件清单、生成者、时机和真实证据规则
  assets/templates/              17份按需填写的Markdown/TXT/JSON模板
evals/                            可复现的离线行为案例与验证说明
docs/handbook.md                  完整通用手册V03，内含文件总表
```

## 安装

下载本仓库或 Release 中的 Skill 压缩包，将完整的 `ai-narrative-workflow` 文件夹放到当前 Codex 的用户技能目录：优先使用 `$CODEX_HOME/skills`，未设置 `CODEX_HOME` 时使用 `~/.codex/skills`。已有同名目录时先保留旧版，再更新。

安装后应是 `skills/ai-narrative-workflow/SKILL.md`，而不是多套一层压缩包目录。让当前客户端重新加载技能；以实际可用技能列表为准。

若环境不支持安装 Skill，可以把 `SKILL.md` 连同 `references/` 与 `assets/` 一起提供给新窗口，并明确要求按技能推进工作。不要只上传入口文件而遗漏相对引用。

## 使用

```text
使用 $ai-narrative-workflow。
项目位置：【当前项目目录】
现有资料：【当前剧本、采用资产及状态记录】
本次目标：【例如只制作第1场的分镜提示词】
本轮范围与授权：【允许做到哪一步、数量/预算/重试等适用限制】
先核现有文件和未结束任务，再完成本轮交付。
```

恢复工作时可以说：

```text
使用 $ai-narrative-workflow 继续这个项目。
先读项目状态与任务台账；已有任务号只恢复查询和下载。
按剩余授权完成工作，说明成果、缺口和下一步。
```

已授权的工作继续执行；Skill本身不授予任何付费生成、额外重抽、定时执行或工程清理权限。用户的当前要求优先于模板和惯例。

## 验证与发布

版本：**1.1.0**。

本版补齐[文件总表](skills/ai-narrative-workflow/references/file-catalog.md)，新增制作锁、连续性、交付说明和7种结构化JSON模板。请求准备工作表不直接发送给API；原始回执和实际提交TXT仍须从真实执行取得。

结构检查和离线行为案例见 [evals/README.md](evals/README.md)。离线案例不调用付费服务，也不宣称验证了任何特定视频模型的效果或API可用性。

本仓库只发布通用方法、模板和虚构验证案例，不包含制作项目的剧本、人物、图片、视频、音色、任务回执或凭证。

## 许可

[MIT](LICENSE)。
