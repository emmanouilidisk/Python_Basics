""" Script for creating and reading a file"""

def main():
    fname = "test.txt"
    txt = open(fname, 'w+')
    txt.write("Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace.Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library. ")
    print(txt.tell())
    txt.seek(0)
    print(txt.tell())
    a = txt.read()
    print(a)
    print(txt.tell())
    
main()
