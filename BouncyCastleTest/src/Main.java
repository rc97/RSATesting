import java.math.BigInteger;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.NoSuchAlgorithmException;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.SecureRandom;
import java.security.Security;
import java.util.HashSet;

import org.bouncycastle.jcajce.provider.asymmetric.rsa.BCRSAPrivateCrtKey;
import org.bouncycastle.jce.provider.BouncyCastleProvider;

public class Main {
	 public static void main(String[] args) throws NoSuchAlgorithmException {
		 
	        //add at runtime the Bouncy Castle Provider
	    	//the provider is available only for this application
	    	Security.addProvider(new BouncyCastleProvider());
	 
	    	//BC is the ID for the Bouncy Castle provider;
	        if (Security.getProvider("BC") == null){
	            System.out.println("Bouncy Castle provider is NOT available");
	        }
	        else{
	            System.out.println("Bouncy Castle provider is available");
	        }
	        
	        testRSABitCount();
	        
	    }
	 
	 public static void testRSABitCount() throws NoSuchAlgorithmException {
		    long start_time = System.nanoTime();
	        KeyPairGenerator rsa = KeyPairGenerator.getInstance("RSA", new BouncyCastleProvider());
	        rsa.initialize(1024, new SecureRandom());
	        int total = 0;
	        
	        int zeroBitsApart = 0, smallD = 0, smallE = 0, sameN = 0, samePorQ = 0;
	        double nsize = 0, psize = 0, qsize = 0, esize = 0, dsize = 0;
	        HashSet<BigInteger> ns = new HashSet<BigInteger>();
	        HashSet<BigInteger> pqs = new HashSet<BigInteger>();
	        int leastDifference = Integer.MAX_VALUE;
	        double differences = 0;
	        int badDiff = 0;
	     
	        while (total < 10000) {
	        	
	        	if (total % 100 == 0 && total != 0){
	        		System.out.println(total);
	        	}
	        	
	            KeyPair keyPair = rsa.generateKeyPair();
	            PrivateKey privateKey = keyPair.getPrivate();
	            BCRSAPrivateCrtKey privateCrtKey = (BCRSAPrivateCrtKey) privateKey;
	            
	            BigInteger p = privateCrtKey.getPrimeP();
	            BigInteger q = privateCrtKey.getPrimeQ();
	            BigInteger n = privateCrtKey.getModulus();
	            BigInteger e = privateCrtKey.getPublicExponent();
	            BigInteger d = privateCrtKey.getPrivateExponent();
	            
	            BigInteger difference = p.subtract(q);
	            if (difference.bitLength() < leastDifference){
	            	leastDifference = difference.bitLength();
	            }
	            
	            differences += difference.bitLength();
	       
	            int diff = Math.abs(p.bitLength() - q.bitLength());
	            if(diff == 0) {
	                zeroBitsApart++;
	            }
	            
	            if (d.bitLength() < (n.bitLength() / 4) && e.compareTo(n) < 0){
	            	smallD++;
	            }
	            
	            if (ns.contains(n)){
	            	sameN++;
	            } else {
	            	ns.add(n);
	            }
	            
	            if (pqs.contains(p)){
	            	samePorQ++;
	            } else {
	            	pqs.add(p);
	            }
	            
	            if (pqs.contains(q)){
	            	samePorQ++;
	            } else {
	            	pqs.add(q);
	            }
	            
	            BigInteger two = new BigInteger("2");
	            if (p.subtract(q).abs().compareTo(two.pow((n.bitLength()/2 - 100))) <= 0){
	            	badDiff++;
	            }
	            
	            total++;
	            nsize += n.bitLength();
	            esize += e.bitLength();
	            dsize += d.bitLength();
	            psize += p.bitLength();
	            qsize += q.bitLength();
	        }
	        double elapsed = (System.nanoTime() - start_time)*Math.pow(10, -9);
	        
	        System.out.println("Total: " + total);
	        System.out.println("Average size of n: " + nsize / 10000);
	        System.out.println("Average size of e: " + esize / 10000);
	        System.out.println("Average size of d: " + dsize / 10000);
	        System.out.println("Average size of p: " + psize / 10000);
	        System.out.println("Average size of q: " + qsize / 10000);
	        
	        System.out.println("Number of keys with p and q 0 bits apart: " + zeroBitsApart);
	        System.out.println("Number of keys small d: " + smallD);
	        System.out.println("Number of keys with repeated n: " + sameN);
	        System.out.println("Number of keys with repeated p or q: " + samePorQ);
	        
	        System.out.println("Time in Seconds: " + elapsed);
	        System.out.println("Least bitlength of difference between p and q: " + leastDifference);
	        System.out.println("Average bitlength of difference between p and q: " + differences/10000);
	        System.out.println("Number of keys which did not follow the NIST standard for difference between p and q: " + badDiff);
    }
	 
	 public static void BigIntegerTest(){
		 BigInteger b = new BigInteger("3034");
		 BigInteger c = new BigInteger("3034");
		 System.out.println("B: " + b.bitCount() + ", " + b.bitLength());
		 System.out.println("C: " + c.bitCount() + ", " + c.bitLength());
		 HashSet<BigInteger> test = new HashSet<BigInteger>();
		 test.add(b);
		 System.out.println(test.contains(c));
	 }
}
