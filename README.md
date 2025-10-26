# MCP Server for Home Assistant Remote Service

This project aims to control a TV via Remote Service provided by [Home Assistant APIs](https://developers.home-assistant.io/docs/api/rest/#post-apiservicesltdomainltservice) using [MCP protocol for Python](https://github.com/modelcontextprotocol/python-sdk).

The MCP exposes a **tool** configured to launch commands for [**Samsung TV**](https://www.home-assistant.io/integrations/samsungtv/)


## Local running

Run the MCP inspector locally:

```bash
uv run mcp dev main.py
```