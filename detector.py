
import re
import ipaddress
from urllib.parse import urlsplit


def analyze_email(email, sender_email=""):

    suspicious_words = [
        "urgent",
        "verify your account",
        "password",
        "click here",
        "account suspended",
        "bank details",
        "won a prize",
        "claim your reward"
    ]

    risk_score = 0
    findings = []

    email_lower = email.lower()

    # Check suspicious words
    for word in suspicious_words:
        if word in email_lower:
            risk_score += 1
            findings.append(
                "Suspicious phrase detected: " + word
            )

    # Check URLs
    urls = re.findall(r'https?://\S+', email_lower)

    shortened_domains = [
        "bit.ly",
        "tinyurl.com",
        "t.co",
        "is.gd",
        "shorturl.at"
    ]

    if urls:
        risk_score += 2

        findings.append(
            "Email contains a URL. Check it carefully."
        )

        for url in urls:

            url = url.rstrip(".,);]")

            try:
                parsed_url = urlsplit(url)
                domain = parsed_url.hostname

                if not domain:
                    continue

                # Check shortened URLs
                if domain.lower() in shortened_domains:
                    risk_score += 2

                    findings.append(
                        "Shortened URL detected: " + domain
                    )

                # Check IP address in URL
                try:
                    ipaddress.ip_address(domain)

                    risk_score += 2

                    findings.append(
                        "URL uses an IP address instead of a domain name."
                    )

                except ValueError:
                    pass

            except ValueError:
                findings.append(
                    "Unable to properly parse a URL."
                )

    # Check sender email address
    if sender_email and "@" in sender_email:

        domain = sender_email.rsplit("@", 1)[1].lower()

        try:
            ipaddress.ip_address(domain)

            risk_score += 2

            findings.append(
                "Sender uses an IP address as its domain."
            )

        except ValueError:
            pass

        # Check punycode domain
        if "xn--" in domain:
            risk_score += 2

            findings.append(
                "Sender domain uses punycode. "
                "Check for possible domain impersonation."
            )

    # Determine risk level
    if risk_score >= 4:
        risk_level = "High Risk"
        explanation = (
            "Multiple suspicious indicators were detected. "
            "Treat this email with caution and verify it independently."
        )

    elif risk_score >= 2:
        risk_level = "Medium Risk"
        explanation = (
            "Some suspicious indicators were detected. "
            "Verify the sender and links before taking action."
        )

    else:
        risk_level = "Low Risk"
        explanation = (
            "No suspicious indicators were detected by the current checks. "
            "This does not guarantee that the email is safe."
        )

    # Return analysis results
    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "explanation": explanation,
        "findings": findings
    }
