from zeep import Client
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("calculator")
wsdl = "http://www.dneonline.com/calculator.asmx?WSDL"
soap_client = Client(wsdl=wsdl)

@mcp.tool()
def add(intA: int, intB: int) -> int:
    """Add two integers.
    
    Args:
        intA: First integer
        intB: Second integer
    """
    result = soap_client.service.Add(intA=intA, intB=intB)
    return result

@mcp.tool()
def multiply(intA: int, intB: int) -> int:
    """Multiply two integers.
    
    Args:
        intA: First integer
        intB: Second integer
    """
    result = soap_client.service.Multiply(intA=intA, intB=intB)
    return result

if __name__ == "__main__":
    mcp.run(transport='stdio')

