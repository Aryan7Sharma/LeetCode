func distributeCandies(n int, limit int) int {
    candyDistCount := 0;
        //i,j,k;
        for i :=0; i<=limit; i++ {
            for j :=0; j<=limit; j++{
                for k :=0; k<=limit; k++ {
                    if(i+j+k == n){
                        candyDistCount+=1;
                    };
                };
            };
        };
    return candyDistCount;
}