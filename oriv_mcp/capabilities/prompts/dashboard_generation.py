from oriv_mcp.server.app import mcp_app

@mcp_app.tool(
    name="get_available_parameters",
    description="Get the list of available parameters for dashboard creation. Call this tool whenever the user asks about the parameters needed for creating a dashboard.",
)
def get_available_parameters() -> list:
    return [{ "speed":"400 "},{"voltage":"10"}]


@mcp_app.tool(
    name="get_live_parameters",
    description="Get the list of live parameters for live parameter data. Call this tool whenever the user wants live parameter data for the dashboard.",
)
def get_live_parameters() -> list:
    return [{"speed":randint(300,550)}]