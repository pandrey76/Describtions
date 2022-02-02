#include <iostream>
#include "stest.hpp"

static void cmd_parse(const int args, const char* argv[]);
static void print_help(std::string aName);

//--------------------------- MAIN ------------------------------------------------------------------------------------
int main(int argc, char* argv[])
{
   if(argc > 1)
    {
        cmd_parse(argc, const_cast<const char**>(argv));
    }

    sTest t{100};

    t.print_i();

    return 0;
}

//---------------------------------------------------------------------------------------------------------------------
static void print_help(std::string aName)
{
    std::cout
        << "Usage: " << aName << " <option(s)>\n"
        << "Options:\n"
        << "\t-h, --hellp   Show this help message\n"
        << "\t-v, --version Show version of program\n"
        << "\t-p, --path    Show paths\n"
        << std::endl;
}
//---------------------------------------------------------------------------------------------------------------------
static void cmd_parse(const int argc, const char* argv[])
{
    for(int i = 1; i < argc; ++i)
    {
        std::string param_name = argv[i];

        if(param_name == "-h" || param_name == "--help")
        {
            print_help(argv[0]);
        }
    }
}