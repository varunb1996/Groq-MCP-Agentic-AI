from tools.filesystem_tool import list_files


def code_agent(directory):

    files = list_files(directory)

    return files[:20]