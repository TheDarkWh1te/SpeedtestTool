
#main speed test module
import speedtest
#for file path 
import os
#for time logging
from datetime import datetime


def run_speedtest():

    #get the speed test object
    test = speedtest.Speedtest()

    # Get the current date and time for logging
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    #vars for printing results to desired path
    #put this ina  diffrent func if theres time
    directory = 'C:/Users/Marley/Desktop'
    filename =  'Speed_Results'
    FilePath = os.path.join(directory, filename)


    # Get the best server based on ping
    test.get_best_server()

    # call funtions within the spped test to get the download & upload speeds + the ping
    download_speed = test.download() / 1_000_000  # Convert to Mbps
    upload_speed = test.upload() / 1_000_000  # Convert to Mbps
    ping = test.results.ping

    # Print the results
    # writes to the resutlts file
    # this can alos be done with 'speedtest-cli > C:\Users\Marley\Desktop\Results.txt' on the cmd line 
    
    # print for testing 
    print(f"Download speed: {download_speed:.2f} Mbps")
    print(f"Upload speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping} ms")

    # format the result as a string
    result_str = f"{timestamp} - Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps, Ping: {ping} ms\n"

    # opens and appands exising test doc with the file path var saves erielr
    # wires results from the speed test with data and time
    with open(FilePath, "a") as doc:
        doc.write(result_str)

if __name__ == "__main__":
    run_speedtest()