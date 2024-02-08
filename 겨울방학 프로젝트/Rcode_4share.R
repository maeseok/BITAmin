setwd("C:/Users/LWG/Desktop/2023/코딩/BITAmin/겨울방학 프로젝트")
install.packages("readxl")
library(readxl)
install.packages("lmtest")
library(lmtest)
install.packages("urca")
library(urca)
install.packages("forecast")
library(forecast)
install.packages("vars")
library(vars)
install.packages("tseries")
library(tseries)

#월별수익률 ts객체 설정
return <- read_xlsx('KCC_monthlyReturn.xlsx', sheet=1)
return <- ts(return[[2]], start = c(2013,1), frequency = 12)
return

#변수 데이터 정상성 검정 및 정상성 객체 설정

#var1

data <- read_xlsx('data.xlsx', sheet=1)

adf.test(data[[2]])
pp.test(data[[2]])

adf.test(diff(data[[2]]))
pp.test(diff(data[[2]]))

var1 <- ts(diff(data[[2]])[3:length(diff(data[[2]]))], start = c(2013,1), frequency = 12)
var1

#var2

adf.test(data[[3]])
pp.test(data[[3]])

adf.test(diff(data[[3]]))
pp.test(diff(data[[3]]))

var2 <- ts(diff(data[[3]])[3:length(diff(data[[3]]))], start = c(2013,1), frequency = 12)
var2

#var3

adf.test(data[[4]])
pp.test(data[[4]])

adf.test(diff(data[[4]]))
pp.test(diff(data[[4]]))

var3 <- ts(diff(data[[4]])[3:length(diff(data[[4]]))], start = c(2013,1), frequency = 12)
var3

#var4

adf.test(data[[5]])
pp.test(data[[5]])

adf.test(diff(data[[5]]))
pp.test(diff(data[[5]]))

var4 <- ts(diff(data[[5]])[3:length(diff(data[[5]]))], start = c(2013,1), frequency = 12)
var4

#var5

adf.test(data[[6]])
pp.test(data[[6]])

adf.test(diff(data[[6]]))
pp.test(diff(data[[6]]))

var5 <- ts(diff(data[[6]])[3:length(diff(data[[6]]))], start = c(2013,1), frequency = 12)
var5

#var6

adf.test(data[[7]])
pp.test(data[[7]])

adf.test(diff(data[[7]]))
pp.test(diff(data[[7]]))

adf.test(diff(diff(data[[7]])))
adf.test(diff(diff(data[[7]])))

var6 <- ts(diff(diff(data[[7]]))[2:length(diff(diff(data[[7]])))], start = c(2013,1), frequency = 12)
var6

#var7

adf.test(data[[8]])
pp.test(data[[8]])

adf.test(diff(data[[8]]))
pp.test(diff(data[[8]]))

adf.test(diff(diff(data[[8]])))
adf.test(diff(diff(data[[8]])))

var7 <- ts(diff(diff(data[[8]]))[2:length(diff(diff(data[[8]])))], start = c(2013,1), frequency = 12)
var7

#var8

adf.test(data[[9]])
pp.test(data[[9]])

adf.test(diff(data[[9]]))
pp.test(diff(data[[9]]))

var8 <- ts(diff(data[[9]])[3:length(diff(data[[9]]))], start = c(2013,1), frequency = 12)
var8

#var9

adf.test(data[[10]])
pp.test(data[[10]])

adf.test(diff(data[[10]]))
pp.test(diff(data[[10]]))

var9 <- ts(diff(data[[10]])[3:length(diff(data[[10]]))], start = c(2013,1), frequency = 12)
var9

#var10

adf.test(data[[11]])
pp.test(data[[11]])

adf.test(diff(data[[11]]))
pp.test(diff(data[[11]]))

var10 <- ts(diff(data[[11]])[3:length(diff(data[[11]]))], start = c(2013,1), frequency = 12)
var10


#var11

adf.test(data[[12]])
pp.test(data[[12]])

adf.test(diff(data[[12]]))
pp.test(diff(data[[12]]))

var11 <- ts(diff(data[[12]])[3:length(diff(data[[12]]))], start = c(2013,1), frequency = 12)
var11

#var12

adf.test(data[[13]])
pp.test(data[[13]])

adf.test(diff(data[[13]]))
pp.test(diff(data[[13]]))

var12 <- ts(diff(data[[13]])[3:length(diff(data[[13]]))], start = c(2013,1), frequency = 12)
var12

#var13

adf.test(data[[14]])
pp.test(data[[14]])

adf.test(diff(data[[14]]))
pp.test(diff(data[[14]]))

var13 <- ts(diff(data[[14]])[3:length(diff(data[[14]]))], start = c(2013,1), frequency = 12)
var13

#var14

adf.test(data[[15]])
pp.test(data[[15]])

adf.test(diff(data[[15]]))
pp.test(diff(data[[15]]))

var14 <- ts(diff(data[[15]])[3:length(diff(data[[15]]))], start = c(2013,1), frequency = 12)
var14

#var15

adf.test(data[[16]])
pp.test(data[[16]])

adf.test(diff(data[[16]]))
pp.test(diff(data[[16]]))

var15 <- ts(diff(data[[16]])[3:length(diff(data[[16]]))], start = c(2013,1), frequency = 12)
var15

#그랜저-인과관계 검정

v1 <- cbind(return, var1)
head(v1)
VARselect(v1, lag.max=12, type='const') # BIC = 1
grangertest(return~var1, order=1) # var1 인과관계x

v2 <- cbind(return, var2)
VARselect(v2, lag.max=12, type='const') # BIC = 2
grangertest(return~var2, order=2) # var2 인과관계x

v3 <- cbind(return, var3)
VARselect(v3, lag.max=12, type='const') # BIC = 1
grangertest(return~var3, order=1) # var3 인과관계x

v4 <- cbind(return, var4)
VARselect(v4, lag.max=12, type='const') # BIC = 3
grangertest(return~var4, order=3) # var4 인과관계x

v5 <- cbind(return, var5)
VARselect(v5, lag.max=12, type='const') # BIC = 2
grangertest(return~var5, order=2) # var5 인과관계x

v6 <- cbind(return, var6)
VARselect(v6, lag.max=12, type='const') # BIC = 3
grangertest(return~var6, order=3) #

v7 <- cbind(return, var7)
VARselect(v7, lag.max=12, type='const') # BIC = 3
grangertest(return~var7, order=3) # var7 인과관계x

v8 <- cbind(return, var8)
VARselect(v8, lag.max=12, type='const') # BIC = 1
grangertest(return~var8, order=1) # var8 인과관계o -> 0.02951

v9 <- cbind(return, var9)
VARselect(v9, lag.max=12, type='const') # BIC = 1
grangertest(return~var9, order=1) # 

v10 <- cbind(return, var10)
VARselect(v10, lag.max=12, type='const') # BIC =
grangertest(return~var10, order=1) # var10 인과관계o -> 0.01197

v11 <- cbind(return, var11)
VARselect(v11, lag.max=12, type='const') # BIC = 1
grangertest(return~var11, order=1) # 

v12 <- cbind(return, var12)
VARselect(v12, lag.max=12, type='const') # BIC = 1
grangertest(return~var12, order=1) # 

v13 <- cbind(return, var13)
VARselect(v13, lag.max=12, type='const') # BIC = 1
grangertest(return~var13, order=1) # var13 인과관계o -> 0.01925

v14 <- cbind(return, var14)
VARselect(v14, lag.max=12, type='const') # BIC = 1
grangertest(return~var14, order=1) # var14 인과관계o -> 0.008534

v15 <- cbind(return, var15)
VARselect(v15, lag.max=12, type='const') # BIC = 1
grangertest(return~var15, order=1) # 


#인과관계가 있는 변수 : var8(경제심리지수), var10(규소가격), var13(건설수주액_경상), var14(건설기성액_경상)

#VAR 모델링

v_final <- cbind(return, var8, var10, var13, var14)
VARselect(v_final, lag.max = 12, type='const')  # BIC = 1
VAR_model <- VAR(v_final, p = 1, type='const')

forecast <- predict(VAR_model, n.ahead=6)
forecast

obs <- window(return, start = c(2013,1))

plot(obs, xlab="", ylab="")
lines(forecast, lty=2)
