<?php

$weeks = array("日","月","火","水","木","金","土");

$count = date("t", mktime(0, 0, 0, 2, 1, 2014));

$dates = array(null);
for ($i = 1; $i < $count+1; $i++) {
    $week_num = date('w', mktime (0, 0, 0, 2, $i, 2014));
    $dates[]['day'] = $weeks[$week_num];
}

print_r($dates);
