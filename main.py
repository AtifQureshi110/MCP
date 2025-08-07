# def main():
#     print("Hello from hello-mcp!")


# if __name__ == "__main__":
#     main()


from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="hello-mcp", stateless_http=True)

mcp_app = mcp.streamable_http_app()
