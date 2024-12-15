'''y <- ts(c(123,39,78,52,110), start=2012)
y
install.packages("ggplot2")
library(ggplot2)
autoplot(melsyd[,"Economy.Class"]) +
  ggtitle("이코노미석 탑승객: 멜버른-시드니") +
  xlab("연도") +
  ylab("탑승객(단위: 1000명)")

install.packages("GGally")
library(GGally)
GGally::ggpairs(as.data.frame(visnights[,1:5]))'''

setwd("C:/Users/gudtj/OneDrive/바탕 화면/2023/코딩/BITAmin/시계열 학습")
tute1 <- read.csv("tute1.csv", header=TRUE)
View(tute1)
mytimeseries <- ts(tute1[,-1], start=1981, frequency=4)
install.packages("ggplot2")
library(ggplot2)
#시계열 데이터는 autoplot error
plot(mytimeseries)
plot(mytimeseries,facets=TRUE)

install.packages("readxl")
library(readxl)
retaildata <- readxl::read_excel("retail.xlsx", skip=1)
myts <- ts(retaildata[,"A3349905J", frequency=12, start=c(1982,4)]) #한해(주기적인 데이터)
View(retaildata)
plot(myts)

install.packages("forecast")
library(forecast)
ggseasonplot(myts) #계절성을 가지지 않아서 x
ggsubseriesplot(myts)
gglagplot(myts) #시간 지연에 따른 관계 (현재와 이전 지점의 값 사이의 관계)
ggAcf(myts) #자기상관함수 (자기상관성이 통계적으로 유의한가? 95%)
