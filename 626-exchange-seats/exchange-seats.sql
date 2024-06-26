# Write your MySQL query statement below
SELECT ROW_NUMBER() OVER() id, student
FROM seat
ORDER BY IF(MOD(id, 2) = 0, id-1, id+1)
#even ids are decreased by 1
#odd ids are increased by 1
#thats how the new ids are generated and it is then ordered by the new ids
