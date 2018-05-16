// topic     : fits read
// reference : CFITSIO User’s Reference Guide
// source    : https://heasarc.gsfc.nasa.gov/docs/software/fitsio/quick/node4.html
// terminal  : clear;gcc fitsread.c -O2 -lcfitsio -lm -pthread;./a.out


#include <string.h>
#include <stdio.h>
#include "fitsio.h"

int main(){

fitsfile        *fptr;
char         card[FLEN_CARD];
int             status = 0;                             /* MUST initialize status */
int             nkeys;
int            ii;

fits_open_file(&fptr, "in.fits", READONLY, &status);
fits_get_hdrspace(fptr, &nkeys, NULL, &status);

    for (ii = 1; ii <= nkeys; ii++) {
    fits_read_record(fptr, ii, card, &status);     /* read keyword */
    printf("%s\n", card);
    }

    printf("END\n\n");     /* terminate listing with END */

    fits_close_file(fptr, &status);

    if (status)     /* print any error messages */
    fits_report_error(stderr, status);


    return(status);
}
