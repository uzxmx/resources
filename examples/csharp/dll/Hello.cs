using System;
using Utility;

namespace HelloWorld
{
    class Hello {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            Hello obj = new Hello();
            obj.Bar();

            Foo foo = new Foo();
            foo.Bar();
        }

        public void Bar()
        {
          Console.WriteLine("Bar");
        }
    }
}
