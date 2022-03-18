using System.CommandLine;

namespace MyApp
{
    class Program
    {
        static void Main(string[] args)
        {
            var rootCmd = new RootCommand("CLI for something");

            var strOpt = new Option<string>(new string[]{"-s", "--string"}, "A string option");
            var intOpt = new Option<int>(
                    "--int",
                    getDefaultValue: () => 42,
                    description: "An option whose argument is parsed as an int");
            var boolOpt = new Option<bool>(
                    "--bool",
                    "An option whose argument is parsed as a bool");
            var fileOpt = new Option<FileInfo>(
                    "--file",
                    "An option whose argument is parsed as a FileInfo");
            var listCmd = new Command("list", "List something")
            {
                strOpt,
                intOpt,
                boolOpt,
                fileOpt,
            };
            listCmd.SetHandler((string str, int i, bool b, FileInfo f) =>
            {
                Console.WriteLine($"Option for -s is: {str}");
                Console.WriteLine($"Option for --int is: {i}");
                Console.WriteLine($"Option for --bool is: {b}");
                Console.WriteLine($"Option --file is: {f?.FullName ?? "null"}");
            }, strOpt, intOpt, boolOpt, fileOpt);
            rootCmd.Add(listCmd);

            rootCmd.Invoke(args);
        }
    }
}
