pprint(it...;sep=" ",ed="\n")=length(it)>0 ? (@inbounds for i in 1:length(it)-1;print(it[i],sep);end;print(last(it),ed)) : print(ed)

function main()
    a,b,c=parse.(Int64, split(readline()))
    count = 0
    while true
        if count>32
            pprint(-1)
            break
        end
        if a%2+b%2+c%2>0
            pprint(count)
            break
        end
        a,b,c=b/2+c/2,a/2+c/2,b/2+c/2
        count+=1
    end
end
main()