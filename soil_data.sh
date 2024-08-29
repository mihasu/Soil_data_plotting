#!/bin/sh
module use /perm/hlam/apps/modulefiles/lmod
module load epygram/1.4.13

DAY=0
LASTDAY=30
MONTH=06
YEAR=2023
CYCLE=00
LASTCYCLE=21
CYCLESTEP=3

while [ $DAY -le $LASTDAY ] ; do
        if [ $DAY -lt 10 ] ; then 
                DAYLL=0$DAY
        else
                DAYLL=$DAY
        fi
        for ((i=$CYCLE; i<=$LASTCYCLE; i+=$CYCLESTEP));
        do     
                if [ $i -lt 10 ] ; then
                       HOURLL=0$i
                else
                       HOURLL=$i
                fi
		
		echo "/$YEAR/$MONTH/$DAYLL/$HOURLL/"
		epy_point.py -f 'X002TG*' -c '26.860820,67.252670' -e 6 -o /path/to/data/$YEAR/$MONTH/$DAYLL/$HOURLL/ICMSHANAL+0000.sfx

		echo "done"     
        done
        DAY=$( expr $DAY + 1 )

done

