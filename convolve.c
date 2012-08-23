#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <sys/time.h>
#include <limits.h>

#ifdef __MACH__
#include <mach/clock.h>
#include <mach/mach.h>
#endif

long get_time_microseconds() {
    /* Adapted from
     * http://stackoverflow.com/questions/275004/c-timer-function-to-provide-time-in-nano-seconds
     */
    struct timespec ts;

#ifdef __MACH__ // OS X does not have clock_gettime, use clock_get_time
    clock_serv_t cclock;
    mach_timespec_t mts;
    host_get_clock_service(mach_host_self(), CALENDAR_CLOCK, &cclock);
    clock_get_time(cclock, &mts);
    mach_port_deallocate(mach_task_self(), cclock);
    ts.tv_sec = mts.tv_sec;
    ts.tv_nsec = mts.tv_nsec;
#else
    clock_gettime(CLOCK_REALTIME, &ts);
#endif

    return (long)ts.tv_sec * 1000 + ts.tv_nsec / 1000;
}


int main(int argc, char **argv) {
    /* Get command line arguments. */
    if (argc < 3) { return 1; }
    char *width_string = argv[1];
    char *height_string = argv[2];

    int width = atoi(width_string);
    int height = atoi(height_string);


    /* Generate a random matrix of size width x height. */
    srand(time(NULL));
    int x, y;
    int **matrix;
    matrix = malloc(height * sizeof(int*));
    for (y=0; y<height; y++) {
        matrix[y] = malloc(width * sizeof(int));
        for (x=0; x<width; x++) {
            matrix[y][x] = rand();
        }
    }

    /*
     * Find max and min convolution values for the kernel [-1, 0, 1], in both
     * the x and y directions.
     */
    long start, finish;
    start = get_time_microseconds();

    int n;
    int dx_max = INT_MIN;
    int dx_min = INT_MAX;
    int dy_max = INT_MIN;
    int dy_min = INT_MAX;
    for (y=0; y<height; y++) {
        for (x=0; x<width-2; x++) {
            n = -matrix[y][x] + matrix[y][x+2];
            if (n > dx_max) {
                dx_max = n;
            }
            if (n < dx_min) {
                dx_min = n;
            }
        }
    }
    for (x=0; x<width; x++) {
        for (y=0; y<height-2; y++) {
            n = -matrix[y][x] + matrix[y+2][x];
            if (n > dy_max) {
                dy_max = n;
            }
            if (n < dy_min) {
                dy_min = n;
            }
        }
    }

    finish = get_time_microseconds();

    /* Display results. */
    printf("dx_max %d\ndx_min %d\ndy_max %d\ndy_min %d\n", dx_max, dx_min, dy_max, dy_min);
    printf("elapsed %fs\n", (finish - start)/1000000.0);

    /* Free matrix memory */
    for (y=0; y<height; y++) {
        free(matrix[y]);
    }
    free(matrix);

    return 0;
}
