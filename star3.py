#      *
#     * *
#    *   *
#   *     *
#  *       *
# ***********




n = int(input())
for i in range(n):
     if i==0 or i==n-1:
        print(' '*(n-i-1) + '*'*(2*i+1))
     else:
        print(' '*(n-i-1) + '*' + ' '*(2*i-1) + '*')




