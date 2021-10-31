import std.stdio : writeln, writefln, readln;
import std.conv;
import std.string : chomp;

int hcf(int a, int b)
{
    while (b != 0)
    {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

unittest
{
    // Sanity checks
    assert hcf(852, 15) == 3;
    assert hcf(5, 4) == 1;
}

int main(string[] args)
{
    // to!int converts to a int, much like int() in python.
    int a, b;
    if (args.length > 2)
    {
        a = to!int(args[1]);
        b = to!int(args[2]);
    }
    else
    {
        writeln("First number: ");
        //Read input and strip whitespace
        a = to!int(chomp(readln));
        writeln("Second number: ");
        b = to!int(chomp(readln));
    }
    writefln("The HCF of %d and %d is: %d", a, b, hcf(a, b));
    return 0;
}
