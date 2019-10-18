str1="sent_no\th_al_%\te_al_%\te_leftover"
str2="sent_no\th_leftover_ids\te_leftover_ids"
str3="sent_no\th_aligned\te_aligned"
echo $str1 > $HOME_anu_tmp/tmp/$1/alignment_percent_info.txt
echo $str2 > $HOME_anu_tmp/tmp/$1/alignment_leftover_info.txt
echo $str3 > $HOME_anu_tmp/tmp/$1/alignment_aligned_info.txt

i=1
n=115 #`ls -d */ | wc -l`
#n=86
current=`pwd`
#echo "$current"
while [ $i -le $n ]
do
        sentence_dir='2.'$i
        echo $sentence_dir
        tmp_path=$HOME_anu_tmp/tmp/$1/$sentence_dir
        python $HOME/8Task/statistic.py  $tmp_path/new_N1.csv $tmp_path/H_wordid-word_mapping.dat $tmp_path/E_lwg.dat #change the path acc. to the location of generate_root.py 
	i=`expr $i + 1`
done
(head -1 $HOME_anu_tmp/tmp/$1/alignment_percent_info.txt && tail -n+2 $HOME_anu_tmp/tmp/$1/alignment_percent_info.txt | sort -k 2gr) > $HOME_anu_tmp/tmp/$1/alignment_percent_info_sorted.txt 
rm $HOME_anu_tmp/tmp/$1/alignment_percent_info.txt
#sed "1i\ $str" $HOME_anu_tmp/tmp/$1/alignment_percent_info_sorted.txt 


