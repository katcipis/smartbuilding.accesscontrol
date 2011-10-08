import sys, traceback, Ice
import Demo

status = 0
ic = None

if len(sys.argv) < 2:
    print ("Usage: {0} <server ip>".format(sys.argv[0]))
    exit()

try:
    ic = Ice.initialize(sys.argv)
    base = ic.stringToProxy("SimplePrinter:tcp -h " + sys.argv[1] + " -p 10000")
    printer = Demo.PrinterPrx.checkedCast(base)
    if not printer:
        raise RuntimeError("Invalid proxy")

    printer.printString("Hello World!")
except:
    traceback.print_exc()
    status = 1

if ic:
    # Clean up
    try:
        ic.destroy()
    except:
        traceback.print_exc()
        status = 1

exit(status)

