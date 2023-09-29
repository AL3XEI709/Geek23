#include <stdio.h>
#include <stdint.h>

// 定义椭圆曲线参数W
#define A_PARAM 4
#define B_PARAM 20
#define P_PARAM 29
#define G_X     13
#define G_Y     23

// 定义椭圆曲线上的点的结构
typedef struct {
    int x;
    int y;
} ECCPoint;
int mod_inverse(int a, int m);


// 计算两个点的加法
ECCPoint ECCAdd(ECCPoint P, ECCPoint Q) {
    ECCPoint R;
    int lambda;

    if (P.x == Q.x && P.y == Q.y) {
        lambda = (3 * P.x * P.x + A_PARAM) % P_PARAM;
        lambda = (lambda * mod_inverse(2 * P.y, P_PARAM)) % P_PARAM;
    } else {
        lambda = (Q.y - P.y) % P_PARAM;
        lambda = (lambda * mod_inverse(Q.x - P.x, P_PARAM)) % P_PARAM;
    }

    R.x = (lambda * lambda - P.x - Q.x) % P_PARAM;
    R.y = (lambda * (P.x - R.x) - P.y) % P_PARAM;

    return R;
}

// 计算点的倍乘
ECCPoint ECCMultiply(ECCPoint P, int k) {
    ECCPoint result = {0, 0};
    ECCPoint Q = P;

    for (int i = 0; i < k-1; i++) {
        result = ECCAdd(result, Q);
    }

    return result;
}


ECCPoint ECCMultiply_min(ECCPoint P, int k) {
    ECCPoint result = {0, 0};
    ECCPoint Q = P;

    for (int i = 0; i < k*(-1); i++) {
        result = ECCAdd(result, Q);
    }
    result.y = (result.y+P_PARAM)%P_PARAM;
    return result;
}

// 计算模逆元素
int mod_inverse(int a, int m) {
    int m0 = m, t, q;
    int x0 = 0, x1 = 1;

    if (m == 1) return 0;

    while (a > 1) {
        q = a / m;
        t = m;
        m = a % m, a = t;
        t = x0;
        x0 = x1 - q * x0;
        x1 = t;
    }

    if (x1 < 0) x1 += m0;

    return x1;
}

int main() {
    ECCPoint basePoint = {G_X, G_Y};
    int privateKey = 25;  // 私钥
    ECCPoint publicKey = ECCMultiply(basePoint, privateKey);

    printf("Public Key: (%d, %d)\n", publicKey.x, publicKey.y);

    // 在实际应用中，这里将使用公钥进行加密，私钥进行解密

    return 0;
}