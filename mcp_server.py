"""MCP stdio server for Sequent Calculus Prover."""
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import SequentProver

def handle_rpc(request):
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "prove_formula_lk",
                        "description": "Automated proof of propositional formula via cut-free Gentzen LK calculus",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "formula": {
                                    "description": "Nested tuple/list format: ['ATOM', 'P'], ['NOT', f], ['AND', f1, f2], ['OR', f1, f2], ['IMP', f1, f2]"
                                }
                            },
                            "required": ["formula"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "prove_formula_lk":
            formula = args.get("formula")
            # Convert lists to tuples recursively
            def to_tuple(x):
                if isinstance(x, list):
                    return tuple(to_tuple(i) for i in x)
                return x
            f = to_tuple(formula)
            valid = SequentProver.prove(f)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"valid": valid, "is_tautology": valid}}
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method {name} not found"}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32600, "message": "Invalid request"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_rpc(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32700, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
