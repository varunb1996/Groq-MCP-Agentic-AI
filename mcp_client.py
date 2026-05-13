from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client


class MCPManager:

    async def connect(self):

        self.session = ClientSession(
            stdio_client("python", ["server.py"])
        )

        await self.session.initialize()


    async def call_tool(self, tool_name, arguments):

        result = await self.session.call_tool(
            tool_name,
            arguments
        )

        return result