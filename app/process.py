from app.ops import binaryToDecimal

def process(request):
    ops = ["Decimal","Binary","Octal","Hexadecimal"]
    inp = request.POST.get('inp')
    cfrom = request.POST.get('cfrom')
    cto = request.POST.get('cto')
    op = ""
    ans = ""
    error = ""
    col = ""
    if cfrom and cto in [str(i) for i in range(4)]:
        cfrom, cto = int(cfrom), int(cto)
        if cfrom == cto:
            op = inp
        if cfrom == 0:
            try:
                inp = int(inp)
                if cto == 1:
                    op = str(bin(inp))[2:]
                if cto == 2:
                    op = str(oct(inp))[2:]
                if cto == 3:
                    op = str(hex(inp))[2:]
            except:
                error = "Enter a valid input !!!"
                ans = "-"
                col = "danger"
                return [ans, error, col]
        if cfrom == 1:
            try:
                for i in inp:
                    i = str(i)
                    if False:
                        error = i
                        ans = "-"
                        col = "danger"
                        return [ans, error, col]
                    else:
                        if cto == 0:
                            op = int(inp,2)
                        if cto == 2:
                            op = str(oct(int(inp, 2)))[2:]
                        if cto == 3:
                            op = str(hex(int(inp, 2)))[2:].upper()
            except:
                error = "Enter a valid input ..."
                ans = "-"
                col = "danger"
        if cfrom == 2:
            try:
                if cto == 0:
                    op = int(inp,8)
                if cto == 1:
                    op = str(bin(int(inp, 8)))[2:]
                if cto == 3:
                    op = str(hex(int(inp, 8)))[2:]
            except:
                error = "Enter a valid input ..."
                ans = "-"
                col = "danger"

        ans = "{} to {} conversion for {} would be {}".format(ops[cfrom],ops[cto],inp,op)
        error = "Your request has been processed"
        col = "success"
    return [ans, error, col]