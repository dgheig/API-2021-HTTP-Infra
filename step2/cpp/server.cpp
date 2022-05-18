#include <iostream>
#include <string>
#include <stdio.h>
#include <time.h>

#include "crow_all.h"

// Get current date/time, format is YYYY-MM-DD.HH:mm:ss
const std::string currentDateTime() {
    time_t     now = time(0);
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    // Visit http://en.cppreference.com/w/cpp/chrono/c/strftime
    // for more information about date/time format
    strftime(buf, sizeof(buf), "%Y-%m-%d %M:%s", &tstruct);

    return buf;
}

int main()
{
    crow::SimpleApp app;

    CROW_ROUTE(app, "/")
    ([]{
        crow::json::wvalue x;
        x["timestamp"] = currentDateTime();
        return x;
    });

    app.port(18080).multithreaded().run();
}
