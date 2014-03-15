csv <- read.csv("Homicides_by_sex2.csv", nrows=193, header=T, encoding="UTF-8")

pdf("homicide.pdf")
par(family="Japan1GothicBBB")

data <- csv$Males.rate.per.100.000

hist(data, breaks=seq(min(data),max(data),(max(data)-min(data))/30), 
    xlim=c(0,140), ylim=c(0,100),
    main="男性殺人被害者数のヒストグラム",
    xlab="男性殺人被害者数", ylab="国数")

dev.next()

data <- log(data[!is.infinite(log(data))])

hist(data, breaks=seq(min(data),max(data),(max(data)-min(data))/30), 
    xlim=c(-2,5), ylim=c(0,14),
    main="男性殺人被害者数の対数ヒストグラム",
    xlab="男性殺人被害者数の対数", ylab="国数")

dev.next()

data <- data.frame(csv$Females.rate.per.100.000, csv$Males.rate.per.100.000)

plot(data,
    xlim=c(0,20), ylim=c(0,140),
    main="女性と男性の殺人被害者数の散布図",
    xlab="女性殺人被害者数", ylab="男性殺人被害者数")

dev.next()

plot(log(data),
    xlim=c(-2,3), ylim=c(-2,5),
    main="女性と男性の殺人被害者数の対数散布図",
    xlab="女性殺人被害者数の対数", ylab="男性殺人被害者数の対数")

dev.off()
