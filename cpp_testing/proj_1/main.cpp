#include <iostream>
#include <filesystem>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <unordered_map>

namespace fs = std::filesystem;

// Simple INI-style configuration parser
std::unordered_map<std::string, std::string> parseConfigFile(const std::string& filename) {
    std::unordered_map<std::string, std::string> config;
    std::ifstream file(filename);

    if (file.is_open()) {
        std::string line;
        while (std::getline(file, line)) {
            line.erase(std::remove_if(line.begin(), line.end(), isspace), line.end()); // Remove whitespace
            if (line.empty() || line[0] == '#' || line[0] == ';') { 
                continue; // Skip comments and empty lines
            }
            auto delimiterPos = line.find("=");
            if (delimiterPos != std::string::npos) {
                std::string key = line.substr(0, delimiterPos);
                std::string value = line.substr(delimiterPos + 1);
                config[key] = value;
            }
        }
    } else {
        std::cerr << "Error: Unable to open configuration file." << std::endl;
    }

    return config;
}

void watchFolder(const std::string& path) {
    fs::path folderToWatch(path);
    fs::file_time_type lastWriteTime = fs::last_write_time(folderToWatch);

    while (true) {
        fs::file_time_type currentWriteTime = fs::last_write_time(folderToWatch);
        if (currentWriteTime != lastWriteTime) {
            // Folder has changed, print the current output
            std::vector<fs::directory_entry> files;
            for (const auto& entry : fs::recursive_directory_iterator(path)) {
                if (entry.is_regular_file()) {
                    files.push_back(entry);
                }
            }

            std::sort(files.begin(), files.end(), [](const auto& a, const auto& b) {
                return a.path() < b.path();
            });

            for (const auto& entry : files) {
                std::cout << entry.path() << std::endl;
            }

            lastWriteTime = currentWriteTime;
        }

        std::this_thread::sleep_for(std::chrono::seconds(1)); // Check every second
    }
}

int main() {
    // Load configuration (you'll need to handle this based on your setup)
    std::unordered_map<std::string, std::string> config = parseConfigFile("config.ini");
    std::string path = config["source_directory"];

    // Start the watch thread in the background
    std::thread watchThread(watchFolder, path);
    watchThread.detach(); // Let it run independently

    // Keep the main thread alive (or do other things here)
    while (true) {
        std::this_thread::sleep_for(std::chrono::seconds(10));
    }

    return 0;
}

