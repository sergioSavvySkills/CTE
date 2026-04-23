---
standard: 127.403-c9C
title: Ethical Issues in Healthcare Technology
lessons: 1
module: 7
status: draft
---

# Ethical Issues in Healthcare Technology

**By the end of this chapter you will be able to:**
- Identify the ethical issues raised by at least three categories of healthcare technology
- Apply the four principles framework to analyze the tradeoffs each technology creates
- Explain why technology raises ethical questions faster than rules and codes can answer them

A 52-year-old man's smartwatch detects an irregular heart rhythm and sends an alert to a health app. He has no symptoms, no doctor appointment scheduled, and no idea whether the reading is accurate. He goes to an urgent care clinic. The provider there has never seen the app's output before, does not know its false-positive rate, and is not sure whether the reading requires a cardiology referral or reassurance. This situation, a real type of case now happening daily across the country, is not a failure of technology. It is an example of technology outrunning the systems designed to use it safely.

### Why technology concentrates ethical questions

Every new capability in healthcare creates new versions of old tensions among autonomy, beneficence, non-maleficence, and justice. The principles themselves do not change. What changes is how fast new applications arrive, and how often they arrive before regulators, professional codes, or clinical training have caught up.

This chapter does not resolve these tensions. The goal here is to name the tradeoffs honestly, identify which principles are at stake in each case, and recognize that reasonable people using the same principles can reach different conclusions. That kind of reasoning is what healthcare ethics education produces.

### Artificial intelligence and algorithmic decision-making

Hospitals and health systems now use AI tools for a wide range of clinical tasks: predicting which patients are at high risk for sepsis, triaging radiology images, estimating a patient's likelihood of being readmitted within 30 days, and flagging medication interactions.

These tools raise a specific justice concern: **algorithmic bias**. In 2019, researchers published a study in *Science* documenting that a widely used US healthcare algorithm systematically underestimated the health needs of Black patients compared to white patients with similar illness severity. The algorithm had been trained on historical spending data, which reflected existing inequities in how care was allocated. The algorithm learned the bias and reproduced it at scale. This is not a hypothetical problem. It was a documented, deployed system affecting millions of patients.

**Automation bias** is a second concern. When a clinical algorithm produces a recommendation, clinicians are prone to over-trusting it, especially under time pressure. A sepsis alert firing on a patient who seems stable creates a real decision: does the clinician override the alert, and on what basis? If the clinician over-trusts the alert and orders aggressive intervention, the patient may be harmed. If the clinician dismisses the alert and the patient does deteriorate, there is a gap in the record between the alert and the lack of response. The clinician remains responsible for the outcome regardless of what the algorithm said.

There is also an autonomy question: does the patient know that an algorithm shaped their care? Most patients do not. Current standards do not require disclosure. Whether that is acceptable is an active ethical and regulatory debate.

[FIGURE: A diagram showing three AI-related ethical risks (algorithmic bias, automation bias, consent gap) mapped to the four principles, with one example question under each]

### Genomics and genetic testing

Genetic testing has moved from research labs to clinical practice to direct-to-consumer products available online. The ethical issues travel with it.

One of the most common issues is the **incidental finding**: a genetic test ordered for one purpose reveals something the patient did not ask about. A panel ordered to look for hereditary cancer syndromes might reveal a variant associated with heart disease, or information about carrier status for a condition the patient's children might inherit. The question of whether to disclose an incidental finding, and how, does not have a uniform answer.

A second issue is that genetic information is inherently about more than the individual being tested. First-degree relatives share roughly 50% of genetic variants. A person who takes a genetic test may generate information with implications for siblings, parents, and children who never consented to be part of any test.

**GINA**, the Genetic Information Nondiscrimination Act, protects genetic information from being used in employment and health insurance underwriting. But GINA does not cover life insurance, disability insurance, or long-term-care insurance. Those gaps are not theoretical, they have consequences for patients making decisions about whether to pursue genetic testing.

### Telehealth and remote monitoring

Telehealth expanded rapidly during and after the COVID-19 pandemic, and it has genuinely improved access for some patients. A rural patient who previously had to drive four hours for a specialist visit can now see that specialist by video. This is a beneficence and justice benefit.

But the **digital divide** cuts against this benefit. Broadband access, device ownership, and digital literacy are not equally distributed. The populations most likely to benefit from telehealth access, rural communities, elderly patients, lower-income households, are also the populations most likely to lack the technology or skills needed to use it. Expanding telehealth without addressing the digital divide may widen the health equity gap rather than narrow it.

Telehealth also limits what a clinician can assess. A physical exam cannot be conducted by video. A patient's skin color, gait, or the sound of their breathing may carry clinical information that the camera misses. The non-maleficence concern is real: a missed finding in a telehealth visit may result in delayed diagnosis.

### Wearables and consumer health technology

Consumer health devices, including smartwatches, connected glucose meters, and direct-to-consumer health monitors, create a new set of concerns. These devices are generally not covered by HIPAA because the companies that make them are not covered entities. The data they collect is governed by the company's terms of service, not by federal health privacy law.

When a person downloads a fitness app or registers a health wearable, the terms of service they accept may permit the company to share that data with employers, advertisers, or researchers. The person may not have read those terms carefully. This is an autonomy issue: consent that exists on paper but not in practice is incomplete consent.

Device accuracy is a non-maleficence concern. Consumer devices vary widely in clinical accuracy. A wearable that generates a "false reassurance," telling a user their heart rhythm is normal when it is not, may prevent someone from seeking care they need. A device that generates a "false alarm" may prompt expensive and unnecessary testing.

### End-of-life technology

Technology has extended the biological functions of life in ways that earlier generations did not face. Mechanical ventilation, ECMO (extracorporeal membrane oxygenation), artificial nutrition and hydration, and dialysis can sustain organ function even when the underlying condition is not recoverable and even when the patient would not have wanted that outcome.

**Advance directives**, including the Texas Directive to Physicians, Medical Power of Attorney, and the **POLST/MOLST** form (Physician Orders for Life-Sustaining Treatment), exist precisely because these technologies require decision-making in advance. A patient who has a signed directive can make their wishes known before losing the capacity to communicate them. A patient without one leaves those decisions to surrogates or to clinicians.

The ethical tensions at the end of life are about autonomy and beneficence in conflict: when a family asks for continued ventilation against a patient's signed directive, they are asserting their version of beneficence ("keep her alive") over the patient's own autonomy ("I do not want machines"). Texas Health and Safety Code Chapter 166 addresses how these conflicts are handled legally. The ethics framework asks how they should be approached with care for everyone involved.

> **Clinical scenario**
>
> A hospital's sepsis-prediction algorithm flags a 68-year-old patient as high risk. The algorithm has a sensitivity of 72% in the general population and 51% in Black patients, a disparity that the hospital's clinical informatics team has not yet corrected. The patient is Black. The attending physician, under time pressure, accepts the alert and orders aggressive fluid resuscitation. The patient had mild dehydration and no sepsis; the intervention causes a brief fluid overload complication. Which of the four principles are at stake? Beneficence, the intent to help. Non-maleficence, the harm caused by the intervention. Justice, the known bias in the tool. And autonomy, the patient was not told that an algorithm with a known racial disparity shaped her care.

### Key terms

**Algorithmic bias:** encoded bias in a clinical algorithm trained on historically skewed data, documented by Obermeyer et al. (2019) in a widely deployed US healthcare algorithm.

**Automation bias:** the failure mode of over-trusting a machine output; a recognized risk of AI tools in clinical settings.

**Incidental finding:** information revealed by a test that the patient did not ask about, such as a BRCA variant found on an unrelated panel.

**Digital divide:** inequitable access to broadband, devices, and digital literacy; a justice issue when telehealth expands access unevenly.

**Advance directive:** a patient's document directing end-of-life technology use; includes directive to physicians, medical power of attorney, and POLST or MOLST forms.

**POLST/MOLST:** Physician or Medical Orders for Life-Sustaining Treatment; portable clinical orders that follow the patient across care settings.

**ECMO:** extracorporeal membrane oxygenation; a technology that can sustain cardiac and pulmonary function, raising autonomy and beneficence questions at end of life.

**GINA:** the Genetic Information Nondiscrimination Act (2008); federal protection against genetic-information discrimination in employment and health insurance, with notable gaps in life and disability insurance.

**21st Century Cures Act:** federal law whose information-blocking rule intersects with patient access to clinical-data technologies.

**Hastings Center:** a leading US bioethics research institute whose reports frame current healthcare technology ethics debates.

### Chapter summary

Healthcare technology creates new versions of the same ethical tensions that have always existed in patient care, but often faster than regulations, professional codes, or clinical training can keep up. Artificial intelligence raises concerns about algorithmic bias, automation bias, and consent. Genomics raises questions about incidental findings and genetic privacy. Telehealth improves access for some while the digital divide excludes others. Consumer health wearables generate data that falls outside HIPAA's protection. End-of-life technology makes advance care planning urgent rather than optional. In each category, the four principles framework (autonomy, beneficence, non-maleficence, justice) is the tool for naming what is at stake and working toward a defensible response.

### Review questions

1. A sepsis-prediction algorithm is shown to have significantly lower sensitivity for Black patients than for white patients. Which of the four ethical principles is most directly violated by continuing to use the algorithm without correction? What would addressing that violation require in practice?
2. A direct-to-consumer genetic test reveals that a 40-year-old woman carries a BRCA1 variant associated with high breast-cancer risk. She did not ask for this information; she took the test to learn about her ancestry. Name the ethical issue this represents and identify which principle it falls under. What obligation, if any, does the company have?
3. A patient in a Texas hospital has a signed advance directive stating she does not want mechanical ventilation if she has a terminal condition. Her adult children are now asking the medical team to place her on a ventilator. Identify the ethical tension, name the principle each party is representing, and describe what Texas law says about how this situation is handled.

### References

- **Obermeyer et al., "Dissecting racial bias in an algorithm used to manage the health of populations," *Science* (2019):** foundational empirical evidence of algorithmic bias in a US healthcare setting.
- **FDA Artificial Intelligence / Machine Learning-enabled medical-device guidance:** regulatory framework for AI in clinical tools.
- **Genetic Information Nondiscrimination Act (GINA, 2008):** federal protections for genetic information in employment and health insurance; scope and limits worth knowing.
- **21st Century Cures Act, Information Blocking rule (ONC, 2020/2022):** patient-access provisions that intersect with emerging clinical-data technologies.
- **American Medical Association *Code of Medical Ethics*, Opinions on AI (5.2) and Telehealth (1.2.12):** profession-level guidance on the technologies above.
- **Hastings Center reports and *American Journal of Bioethics*:** accessible peer-reviewed sources for current bioethics debates in emerging technology.
- **CMS Interoperability and Patient Access final rules:** federal rules shaping data access for patients and apps.
- **Beauchamp and Childress, *Principles of Biomedical Ethics*:** the four-principles framework for structuring the discussion.
