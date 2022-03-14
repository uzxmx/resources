using System;

namespace HelloWorld
{
    class Hello {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            Hello obj = new Hello();
            obj.Foo();
            obj.Bar();
        }

        public void Foo()
        {
          Console.WriteLine("Foo");
        }

        public void Bar()
        {
          Console.WriteLine("Bar");
        }
    }
}
