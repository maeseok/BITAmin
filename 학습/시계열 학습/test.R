y <- ts(c(123,39,78,52,110), start=2012)
y
install.packages("ggplot2")
library(ggplot2)
autoplot(melsyd[,"Economy.Class"]) +
  ggtitle("이코노미석 탑승객: 멜버른-시드니") +
  xlab("연도") +
  ylab("탑승객(단위: 1000명)")

install.packages("GGally")
library(GGally)
GGally::ggpairs(as.data.frame(visnights[,1:5]))