# AISEC 智能体安全分析平台

## 项目介绍

AISEC 是一个面向 AI Agent 的安全评估平台。

平台可以对用户输入的：

- 智能体任务
- Agent代码
- Prompt行为

进行自动分析，并检测：

1 AI安全风险  
2 代码漏洞  
3 Prompt Injection  
4 行为风险  
5 潜在法律风险  

系统基于：

- FastAPI
- React
- DeepSeek LLM

构建。

---

## 系统架构

用户

↓

前端 React 平台

↓

FastAPI API网关

↓

AI分析模块

- 安全分析Agent
- 法律风险Agent
- 行为路径Agent
- Prompt攻击检测Agent

↓

DeepSeek大模型

↓

返回安全报告

---

## 启动方式

安装 Docker

运行：

docker-compose up --build

访问：

http://localhost:3000

API：

http://localhost:8000