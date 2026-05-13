from tools.filesystem_tool import list_files
from tools.retrieval_tool import retrieve_context

TOOLS = {
    "filesystem": list_files,
    "retrieval": retrieve_context
}