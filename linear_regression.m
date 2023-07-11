clear
clc
%%
data = importdata("chirps-modified.txt");

X = data(:,1);

Y = data(:,2);

n = 2;

Xp = powers(X,0,n);

Yp = powers(Y,1,1);

Xpt = Xp';

a = inv((Xpt*Xp))* (Xpt*Yp) ;

Y2 = [];
for i = 1 : numel(X)

    Y2(i) = evalValue(a,X(i));

end

scatter(X,Y,Marker="*")

hold on 

plot(X,Y2)







%%
function value = evalValue(a,x)

value = 0;

for i =1 : length(a)

    value = value + (a(i) * (x^(i-1)));

end

end
%%
function result = powers(arr,lower_pow,upper_pow)

result = zeros(length(arr),(upper_pow-lower_pow+1));

for i = 1 : length(result(1,:))

    if lower_pow ==0 
        lower_pow = 1;
        upper_pow = upper_pow +1;
    end

    for j = lower_pow : upper_pow
        
       result(i,j) = arr(i)^(j-1);
    end

end
end