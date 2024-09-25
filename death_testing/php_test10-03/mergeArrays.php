<?php

$multiDimensionalArray = [[1], [1, 2]];
$singleDimensionalArray = [];

foreach($multiDimensionalArray as $array) {
    $singleDimensionalArray = array_merge($singleDimensionalArray, $array);
}

print_r($singleDimensionalArray);

?>
