#include <iostream>
#include <string>
using namespace std;

string getLongestRegex(const string &a, const string &b, const string &c) {
    int n = a.size();
    int mismatchIndex = -1;

    // Find the first mismatch index
    for (int i = 0; i < n; ++i) {
        if (c[i] != a[i] && c[i] != b[i]) {
            mismatchIndex = i;
            break;
        }
    }

    // If no mismatch is found, return "-1"
    if (mismatchIndex == -1) {
        return "-1";
    }

    // Construct the regex
    string placementlelo;
    for (int i = 0; i < n; ++i) {
        if (i == mismatchIndex) {
            placementlelo += "[^" + string(1, a[i]) + string(1, b[i]) + "]";
        } else {
            placementlelo += "[ABCDEFGHIJKLMNOPQRSTUVWXYZ]";
        }
    }
    return placementlelo;
}

int main() {
    // Example usage
    string a = "AXBYCZ";
    string b = "AXDYCZ";
    string c = "AXEYCZ";
    cout << "Regex: " << getLongestRegex(a, b, c) << endl;
    return 0;
}

