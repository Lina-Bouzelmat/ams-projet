set datafile separator '\t'
set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set format x "%H:%M\n%d-%m"
set term png size 1000,600
set output "/home/uapv2202351/scripts/evolution_graph.png"
set title "Évolution CPU et RAM"
set xlabel "Temps"
set ylabel "Utilisation (%)"
set grid
plot "/tmp/metrics.tsv" using 1:2 title "CPU" with lines lw 2, \
     "" using 1:3 title "RAM" with lines lw 2
