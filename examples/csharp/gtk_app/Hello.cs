using Gtk;
using System;

namespace HelloWorld
{
  class Hello
  {
    static void Main()
    {
      Application.Init();

      Window window = new Window("Hello Mono World");
      window.Show();

      Application.Run();
    }
  }
}
