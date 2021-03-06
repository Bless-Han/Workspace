public class PrimitiveTypeTest {
	public static void main(String[] args) {
		// byte
		System.out.println("基本类型：byte" + Byte.SIZE);
		System.out.println("包装类：java.lang.Byte");
		System.out.println("最小值：Byte.MIN_VALUE=" + Byte.MIN_VALUE);
		System.out.println("最大值：Byte.MIN_VALUE=" + Byte.MAX_VALUE);

		// short
		System.out.println("基本类型：short" + Short.SIZE);
		System.out.println("包装类：java.lang.Short");
		System.out.println("最小值：Short.MIN_VALUE=" + Short.MIN_VALUE);
		System.out.println("最大值：Short.MIN_VALUE=" + Short.MAX_VALUE);

		// int
		System.out.println("基本类型：int" + Integer.SIZE);
		System.out.println("包装类：java.lang.Integer");
		System.out.println("最小值：Integer.MIN_VALUE=" + Integer.MIN_VALUE);
		System.out.println("最大值：Integer.MIN_VALUE=" + Integer.MAX_VALUE);

		// long
		System.out.println("基本类型：long" + Long.SIZE);
		System.out.println("包装类：java.lang.Long");
		System.out.println("最小值：Long.MIN_VALUE=" + Long.MIN_VALUE);
		System.out.println("最大值：Long.MIN_VALUE=" + Long.MAX_VALUE);

		// float
		System.out.println("基本类型：float" + Float.SIZE);
		System.out.println("包装类：java.lang.Float");
		System.out.println("最小值：Float.MIN_VALUE=" + Float.MIN_VALUE);
		System.out.println("最大值：Float.MIN_VALUE=" + Float.MAX_VALUE);

		// double
		System.out.println("基本类型：double" + Double.SIZE);
		System.out.println("包装类：java.lang.Double");
		System.out.println("最小值：Double.MIN_VALUE=" + Double.MIN_VALUE);
		System.out.println("最大值：Double.MIN_VALUE=" + Double.MAX_VALUE);

		// char
		System.out.println("基本类型：char 二进制位数:" + Character.SIZE);
		System.out.println("包装类：java.lang.Character");
		System.out.println("最小值：Character.MIN_VALUE=" +
				(int) Character.MIN_VALUE);
		System.out.println("最大值：Character.MIN_VALUE=" +
				(int) Character.MAX_VALUE);
	}
}
