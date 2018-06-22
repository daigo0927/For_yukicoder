// This is completely copied from answer #264206
// I think the given time limit is a little strict ...
import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class No697 implements Runnable {
	public static void main(String[] args) {
		new Thread(null, new No697(), "", Runtime.getRuntime().maxMemory()).run();
	}

	class DJSet {
		int n;
		int[] upper;

		public DJSet(int n_) {
			n = n_;
			upper = new int[n];
			Arrays.fill(upper, -1);
		}

		int root(int x) {
			return upper[x] < 0 ? x : (upper[x] = root(upper[x]));
		}

		boolean equiv(int x, int y) {
			return root(x) == root(y);
		}

		void setUnion(int x, int y) {
			x = root(x);
			y = root(y);
			if (x == y)
				return;
			if (upper[x] > upper[y]) {
				x ^= y;
				y ^= x;
				x ^= y;
			}
			upper[x] += upper[y];
			upper[y] = x;
		}
	}

	public void run() {
		FastScanner sc = new FastScanner();
		int H = sc.nextInt();
		int W = sc.nextInt();
		DJSet ds = new DJSet(H * W);
		int[][] A = new int[H][W];
		for (int i = 0; i < H; ++i) {
			for (int j = 0; j < W; ++j) {
				A[i][j] = sc.nextInt();
			}
		}
		for (int i = 0; i < H; ++i) {
			for (int j = 0; j < W; ++j) {
				if (A[i][j] != 1)
					continue;
				for (int di = -1; di <= 1; ++di) {
					for (int dj = -1; dj <= 1; ++dj) {
						if (Math.abs(di) + Math.abs(dj) != 1)
							continue;
						int ni = i + di;
						int nj = j + dj;
						if (ni < 0 || nj < 0 || ni >= H || nj >= W)
							continue;
						if (A[ni][nj] != 1)
							continue;
						ds.setUnion(i * W + j, ni * W + nj);
					}
				}
			}
		}
		int cnt = 0;
		for (int i = 0; i < H; ++i) {
			for (int j = 0; j < W; ++j) {
				if (A[i][j] == 1 && i * W + j == ds.root(i * W + j))
					++cnt;
			}
		}
		System.out.println(cnt);

	}

	class FastScanner {
		private final InputStream in = System.in;
		private final byte[] buffer = new byte[1024];
		private int ptr = 0;
		private int buflen = 0;

		private boolean hasNextByte() {
			if (ptr < buflen) {
				return true;
			} else {
				ptr = 0;
				try {
					buflen = in.read(buffer);
				} catch (IOException e) {
					e.printStackTrace();
				}
				if (buflen <= 0) {
					return false;
				}
			}
			return true;
		}

		private int readByte() {
			if (hasNextByte())
				return buffer[ptr++];
			else
				return -1;
		}

		private boolean isPrintableChar(int c) {
			return 33 <= c && c <= 126;
		}

		public boolean hasNext() {
			while (hasNextByte() && !isPrintableChar(buffer[ptr]))
				ptr++;
			return hasNextByte();
		}

		public String next() {
			if (!hasNext())
				throw new NoSuchElementException();
			StringBuilder sb = new StringBuilder();
			int b = readByte();
			while (isPrintableChar(b)) {
				sb.appendCodePoint(b);
				b = readByte();
			}
			return sb.toString();
		}

		public long nextLong() {
			if (!hasNext())
				throw new NoSuchElementException();
			long n = 0;
			boolean minus = false;
			int b = readByte();
			if (b == '-') {
				minus = true;
				b = readByte();
			}
			if (b < '0' || '9' < b) {
				throw new NumberFormatException();
			}
			while (true) {
				if ('0' <= b && b <= '9') {
					n *= 10;
					n += b - '0';
				} else if (b == -1 || !isPrintableChar(b)) {
					return minus ? -n : n;
				} else {
					throw new NumberFormatException();
				}
				b = readByte();
			}
		}

		public int nextInt() {
			long nl = nextLong();
			if (nl < Integer.MIN_VALUE || nl > Integer.MAX_VALUE)
				throw new NumberFormatException();
			return (int) nl;
		}

		public double nextDouble() {
			return Double.parseDouble(next());
		}
	}

	void tr(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}
}
