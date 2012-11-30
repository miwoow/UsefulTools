#!/bin/sh

files=`ls .`
for f in ${files};
do
    echo ${f}
    rename 's/^\d+\.第(\d{1})章?/000$1.第000$1章/' ${f}
    rename 's/^\d+\.第(\d{2})章?/00$1.第00$1章/' ${f}
    rename 's/^\d+\.第(\d{3})章?/0$1.第0$1章/' ${f}
done

