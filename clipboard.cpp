/* clipboard.cpp
 *
 * Simple program to read stdin and copy it to the clipboard
*/

#include <iostream>
#include <istream>
#include <ostream>
#include <iomanip>
#include <string>
#include <sstream>

#include "my_windows.h"

using namespace std;

//Since we're using the Win32 API - hard code the line ending
static const string LINEEND = "\r\n";


static int show_help() {
    cout << "clipboard [-i|-o|-?]" << endl
         << "  -?  Show this message" << endl
         << "  -i  Copy stdin to clipboard" << endl
         << "  -o  Copy clipboard to stdout" << endl
         << endl
         << " DEFAULT ACTION is to read stdin to clipboard" << endl
         << endl;
    return 1;
}


static int in_to_clip() {
    string line;
    stringstream buffer;
    while(getline(cin, line)) {
        buffer << line << LINEEND;
    }
    
    string output = buffer.str();
    size_t bufsize = output.size() + 1; //Include trailing NULL
    buffer.str("");
            
    HGLOBAL bufLock = GlobalAlloc(GMEM_MOVEABLE, bufsize);
    memcpy(GlobalLock(bufLock), output.c_str(), bufsize);
    GlobalUnlock(bufLock);
    
    OpenClipboard(NULL);
    EmptyClipboard();
    SetClipboardData(CF_TEXT, bufLock);
    CloseClipboard();
    
    return 0;
}


static int clip_to_out() {
    OpenClipboard(NULL);
    HANDLE clipdata = GetClipboardData(CF_TEXT);
    string clipstr = string((char*)clipdata);
    CloseClipboard();
    cout << clipstr << flush;
    return 0;
}


int main(int argc, char* argv[]) {
    if (argc > 2) {
        //More than argv[0] and one option
        return show_help();
    }
    
    for (int i = 1; i < argc; ++i) {
        string arg = argv[i];
        if      (arg == "-?") return show_help();
        else if (arg == "-i") return in_to_clip();
        else if (arg == "-o") return clip_to_out();
    }
    
    
    if (argc <= 1) {
        //Default action
        return in_to_clip();
    }
    else {
        //Command line options, but nothing found
        return show_help();
    }
}
