pprint(it...;sep=" ",ed="\n")=length(it)>0 ? (@inbounds for i in 1:length(it)-1;print(it[i],sep);end;print(last(it),ed)) : print(ed)

n=parse(Int64, readline())
pprint((n)*(n-1)÷2)
