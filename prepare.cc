#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <filesystem>

int main()
{
    std::filesystem::path directory("/path/to/directory");
    if (std::filesystem::exists(directory))
    {
        std::cout << "Directory exists" << std::endl;
    }
    else
    {
        std::cout << "Directory does not exist" << std::endl;
    }
    return 0;
}