class DES():
    def __init__(self):
        #IP置换表
        self.IP_table=[58, 50, 42, 34, 26, 18, 10,  2,
          60, 52, 44, 36, 28, 20, 12,  4,
          62, 54, 46, 38, 30, 22, 14,  6,
          64, 56, 48, 40, 32, 24, 16,  8,
          57, 49, 41, 33, 25, 17,  9,  1,
          59, 51, 43, 35, 27, 19, 11,  3,
          61, 53, 45, 37, 29, 21, 13,  5,
          63, 55, 47, 39, 31, 23, 15,  7
        ]

        # 逆IP置换表
        self._IP_table = [40, 8, 48, 16, 56, 24, 64, 32,
                     39, 7, 47, 15, 55, 23, 63, 31,
                     38, 6, 46, 14, 54, 22, 62, 30,
                     37, 5, 45, 13, 53, 21, 61, 29,
                     36, 4, 44, 12, 52, 20, 60, 28,
                     35, 3, 43, 11, 51, 19, 59, 27,
                     34, 2, 42, 10, 50, 18, 58, 26,
                     33, 1, 41, 9, 49, 17, 57, 25
                     ]
        # S盒中的S1盒
        self.S1 = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
              0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
              4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
              15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13
              ]
        # S盒中的S2盒
        self.S2 = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
              3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
              0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
              13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9
              ]
        # S盒中的S3盒
        self.S3 = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
              13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
              13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
              1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12
              ]
        # S盒中的S4盒
        self.S4 = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
              13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
              10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
              3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14
              ]
        # S盒中的S5盒
        self.S5 = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
              14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
              4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
              11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3
              ]
        # S盒中的S6盒
        self.S6 = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
              10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
              9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
              4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13
              ]
        # S盒中的S7盒
        self.S7 = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
              13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
              1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
              6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12
              ]
        # S盒中的S8盒
        self.S8 = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
              1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
              7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
              2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11
              ]
        # S盒
        self.S = [self.S1, self.S2,self.S3,self.S4,self.S5,self.S6,self.S7,self.S8]
        # P盒
        self.P_table = [16, 7, 20, 21,
                   29, 12, 28, 17,
                   1, 15, 23, 26,
                   5, 18, 31, 10,
                   2, 8, 24, 14,
                   32, 27, 3, 9,
                   19, 13, 30, 6,
                   22, 11, 4, 25
                   ]
        # 压缩置换表1，不考虑每字节的第8位，将64位密钥减至56位。然后进行一次密钥置换。
        self.compression_table1 = [57, 49, 41, 33, 25, 17, 9,
                        1, 58, 50, 42, 34, 26, 18,
                        10, 2, 59, 51, 43, 35, 27,
                        19, 11, 3, 60, 52, 44, 36,
                        63, 55, 47, 39, 31, 23, 15,
                        7, 62, 54, 46, 38, 30, 22,
                        14, 6, 61, 53, 45, 37, 29,
                        21, 13, 5, 28, 20, 12, 4
                        ]

        # 压缩置换表2，用于将循环左移和右移后的56bit密钥压缩为48bit
        self.compression_table2 = [14, 17, 11, 24, 1, 5,
                        3, 28, 15, 6, 21, 10,
                        23, 19, 12, 4, 26, 8,
                        16, 7, 27, 20, 13, 2,
                        41, 52, 31, 37, 47, 55,
                        30, 40, 51, 45, 33, 48,
                        44, 49, 39, 56, 34, 53,
                        46, 42, 50, 36, 29, 32
                        ]

        # 用于对数据进行扩展置换，将32bit数据扩展为48bit
        self.extend_table = [32, 1, 2, 3, 4, 5,
                        4, 5, 6, 7, 8, 9,
                        8, 9, 10, 11, 12, 13,
                        12, 13, 14, 15, 16, 17,
                        16, 17, 18, 19, 20, 21,
                        20, 21, 22, 23, 24, 25,
                        24, 25, 26, 27, 28, 29,
                        28, 29, 30, 31, 32, 1
                        ]



    #将char转化为unicode
    def char2unicode_ascii(self,input):
        output = []
        for i in range(len(input)):
            output.append(ord(input[i]))
        return output

    # 将Unicode码转为bit
    def unicode2bit(self,input):
        output = []
        for i in range(len(input) * 16):
            output.append((input[int(i / 16)] >> (i % 16)) & 1)  # 一次左移一bit
        return output

    # 将8位ASCII码转为bit
    def byte2bit(self,input):
        output = []
        for i in range(len(input) * 8):
            output.append((input[int(i / 8)] >> (i % 8)) & 1)  # 一次左移一bit
        return output

    # 将bit转为Unicode码
    def bit2unicode(self,input):
        output = []
        temp = 0
        for i in range(len(input)):
            temp = temp | (input[i] << (i % 16))
            if i % 16 == 15:
                output.append(temp)
                temp = 0
        return output

    # 将bit转为ascii 码
    def bit2byte(self,input):
        output = []
        temp = 0
        for i in range(len(input)):
            temp = temp | (input[i] << (i % 8))
            if i % 8 == 7:
                output.append(temp)
                temp = 0
        return output

    # 将unicode码转为字符（中文或英文）
    def unicode2char(self,input):
        output = ""
        for i in range(len(input)):
            output = output + chr(input[i])
        return output



    def DES(self,text, key, mode):

        #生成所有key
        keys = []
        asciikey = self.char2unicode_ascii(key)
        keyinit = self.byte2bit(asciikey)
        # 初始化列表key0,key1
        key0 = [0 for i in range(56)]
        key1 = [0 for i in range(48)]
        # 进行密码压缩置换1，将64位密码压缩为56位
        for i in range(56):
            key0[i] = keyinit[self.compression_table1[i] - 1]

        # 进行16轮的密码生成
        for i in range(16):
            # 根据表格可知，当i=0或i=8或i=15时移动步数为1，其余情况为2
            if (i == 0 or i == 1 or i == 8 or i == 15):
                moveStep = 1
            else:
                moveStep = 2

            # 循环左移
            for j in range(moveStep):
                for k in range(8):
                    temp = key0[k * 7]
                    for m in range(7 * k, 7 * k + 6):
                        key0[m] = key0[m + 1]
                    key0[k * 7 + 6] = temp
                temp = key0[0]
                for k in range(27):
                    key0[k] = key0[k + 1]
                key0[27] = temp
                temp = key0[28]
                for k in range(28, 55):
                    key0[k] = key0[k + 1]
                key0[55] = temp

            # 56位key变为48位
            for k in range(48):
                key1[k] = key0[self.compression_table2[k] - 1]
            keys.extend(key1)



        finalTextOfBit = [0 for i in range(64)]

        # 加密操作
        if mode == 0:

            extendR = [0 for i in range(48)]  # 用于盛放R部分的扩展结果
            unicodeText = self.char2unicode_ascii(text)
            bitText = self.unicode2bit(unicodeText)
            initTrans = [0 for i in range(64)]  # 初始化，用于存放IP置换后的结果

            # ------------------进行初始IP置换---------------
            for i in range(64):
                initTrans[i] = bitText[self.IP_table[i] - 1]
            # 将64位明文分为左右两部分
            L = [initTrans[i] for i in range(32)]
            R = [initTrans[i] for i in range(32, 64)]

            # 16轮迭代
            for i in range(16):
                tempR = R  # 用于临时盛放R

                # -----------进行扩展，将32位扩展为48位--------
                for j in range(48):
                    extendR[j] = R[self.extend_table[j] - 1]
                #           print(len(keyResult))
                keyi = [keys[j] for j in range(i * 48, i * 48 + 48)]
                # ----------与key值进行异或运算----------------
                XORResult = [0 for j in range(48)]
                for j in range(48):
                    if keyi[j] != extendR[j]:
                        XORResult[j] = 1

                SResult = [0 for k in range(32)]
                # ---------开始进行S盒替换-------------------
                for k in range(8):
                    row = XORResult[k * 6] * 2 + XORResult[k * 6 + 5]
                    column = XORResult[k * 6 + 1] * 8 + XORResult[k * 6 + 2] * 4 + XORResult[k * 6 + 3] * 2 + \
                             XORResult[k * 6 + 4]
                    temp = self.S[k][row * 16 + column]
                    for m in range(4):
                        SResult[k * 4 + m] = (temp >> m) & 1
                # -----------------------------------------
                PResult = [0 for k in range(32)]
                # --------------开始进行P盒置换----------------
                for k in range(32):
                    PResult[k] = SResult[self.P_table[k] - 1]
                # ------------------------------------------

                # --------------与L部分的数据进行异或------------
                XORWithL = [0 for k in range(32)]
                for k in range(32):
                    if L[k] != PResult[k]:
                        XORWithL[k] = 1
                # ----------------------------------------------

                # -------------将临时保存的R部分值，即tempR复制给L------
                L = tempR
                R = XORWithL

            # ----交换左右两部分------
            L, R = R, L

            # -----合并为一部分
            tempText = L
            tempText.extend(R)
            # -----------IP逆置换--------
            for k in range(64):
                finalTextOfBit[k] = tempText[self._IP_table[k] - 1]
            finalTextOfUnicode = self.bit2byte(finalTextOfBit)
            finalTextOfChar = self.unicode2char(finalTextOfUnicode)
            return finalTextOfChar




        # 解密操作
        else:

            extendR = [0 for i in range(48)]  # 用于盛放R部分的扩展结果
            unicodeText = self.char2unicode_ascii(text)
            bitText = self.byte2bit(unicodeText)

            initTrans = [0 for i in range(64)]  # 初始化，用于存放IP置换后的结果

            # ------------------进行初始IP置换---------------
            for i in range(64):
                initTrans[i] = bitText[self.IP_table[i] - 1]
            # 将64位明文分为左右两部分
            L = [initTrans[i] for i in range(32)]
            R = [initTrans[i] for i in range(32, 64)]

            # -----------------开始16轮的循环-----------------
            for i in range(15, -1, -1):
                tempR = R  # 用于临时盛放R

                # -----------进行扩展，将32位扩展为48位--------
                for j in range(48):
                    extendR[j] = R[self.extend_table[j] - 1]

                keyi = [keys[j] for j in range(i * 48, i * 48 + 48)]
                # ----------与key值进行异或运算----------------
                XORResult = [0 for j in range(48)]
                for j in range(48):
                    if keyi[j] != extendR[j]:
                        XORResult[j] = 1

                SResult = [0 for k in range(32)]
                # ---------开始进行S盒替换-------------------
                for k in range(8):
                    row = XORResult[k * 6] * 2 + XORResult[k * 6 + 5]
                    column = XORResult[k * 6 + 1] * 8 + XORResult[k * 6 + 2] * 4 + XORResult[k * 6 + 3] * 2 + \
                             XORResult[k * 6 + 4]
                    temp = self.S[k][row * 16 + column]
                    for m in range(4):
                        SResult[k * 4 + m] = (temp >> m) & 1
                # -----------------------------------------
                PResult = [0 for k in range(32)]
                # --------------开始进行P盒置换----------------
                for k in range(32):
                    PResult[k] = SResult[self.P_table[k] - 1]
                # ------------------------------------------

                # --------------与L部分的数据进行异或------------
                XORWithL = [0 for k in range(32)]
                for k in range(32):
                    if L[k] != PResult[k]:
                        XORWithL[k] = 1
                # ----------------------------------------------

                # -------------将临时保存的R部分值，即tempR复制给L------
                L = tempR
                R = XORWithL

            # ----交换左右两部分------
            L, R = R, L

            # -----合并为一部分
            tempText = L
            tempText.extend(R)
            # -----------IP逆置换--------
            for k in range(64):
                finalTextOfBit[k] = tempText[self._IP_table[k] - 1]
            finalTextOfUnicode = self.bit2unicode(finalTextOfBit)
            finalTextOfChar = self.unicode2char(finalTextOfUnicode)
            return finalTextOfChar


    def encrypt(self,text,key):
        Result = ""
        length = len(text)
        text = text + (length % 4) * " "
        length = len(text)

        print("加密后的文本：", end=" ")
        for i in range(int(length / 4)):
            tempText = [text[j] for j in range(i * 4, i * 4 + 4)]
            Result = "".join([Result, self.DES(tempText, key, 0)])
        return Result


    def decrypt(self,text,key):
        length = len(text)
        Result = ""
        for i in range(int(length / 8)):
            tempText = [text[j] for j in range(i * 8, i * 8 + 8)]
            Result = "".join([Result, self.DES(tempText, key,1)])
        return Result


if __name__ == '__main__':
    t = DES()
    text = input("请输入要操作的文本:  ")
    print(" ".join(["输入的文本时", text]))
    optionType = input("请选择是进行加密还是解密，加密输入0，解密输入1:  ")
    while (not (optionType == '0' or optionType == '1')):
        print("Wrong!!!选择的操作类型只能是0或者是1")
        optionType = input("请选择是进行加密还是解密，加密输入0，解密输入1:  ")
    length = len(text)

    Result = ""
    if optionType == '0':

        # ----------若输入文本的长度不是4的整数倍，即不是64字节的整数倍，用空格补全（此处为了加密中文，用的是unicode编码，即用16字节表示一个字符）-------
        text = text + (length % 4) * " "
        length = len(text)
        key = input("请输入8位加密密码: ")

        while (len(key) != 8):
            print("wrong!!请输入8位密码")
            key = input("请输入8位加密密码: ")

        print(t.encrypt(text, key))
        #
        # print("加密后的文本：", end=" ")
        # for i in range(int(length / 4)):
        #     tempText = [text[j] for j in range(i * 4, i * 4 + 4)]
        #     Result = "".join([Result, t.DES(tempText, key, int(optionType))])
        # #            f.write(Result)
        # print(Result)

    if optionType == '1':
        # ----------若输入文本的长度不是8的整数倍，即不是64字节的整数倍，用空格补全（此处解密出来的密文用的是每8bit转换为一个ascii码，所以生成的八位表示的字符）-------
        length = len(text)
        key = input("请输入8位解密密码: ")
        while (len(key) != 8):
            print("wrong!!请输入8位密码")
            key = input("请输入8位解密密码: ")

        print("解密后的文本：", end=" ")
        print(t.decrypt(text,key))
        # for i in range(int(length / 8)):
        #     tempText = [text[j] for j in range(i * 8, i * 8 + 8)]
        #     Result = "".join([Result, t.DES(tempText, key, int(optionType))])
        # print(Result)