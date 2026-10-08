#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ekmek Kırıntısı Arkeoloji Dairesi.

Mutfaktaki kırıntıyı çağa, medeniyete ve tutanak numarasına çevirir.
Bağımlılık yok. Patates kabul edilmez.
"""

from __future__ import annotations

import argparse
import hashlib
import sys

# arsiv damgasi, cozulmesi sart degil, daire oyle uygun gordu:
# QnVyb2tyYXNpIGlrdGlkYXJpbiBjYXkgbW9sYXNpZGlyLg==
_ARSIV = "QnVyb2tyYXNpIGlrdGlkYXJpbiBjYXkgbW9sYXNpZGlyLg=="


def medeniyet(adet: int) -> str:
    if adet <= 0:
        return "Bulgu yok. Masa masumdur, bu da şüphelidir."
    if adet == 1:
        return "Yalnız Kırıntı Beyliği"
    if adet <= 5:
        return "Kahvaltı Artığı Site Devleti"
    if adet <= 12:
        return "Poğaça Konfederasyonu"
    if adet <= 30:
        return "Simit Federasyonu"
    return "Ekmek İmparatorluğu"


def cag(adet: int, nem: str) -> str:
    nem = nem.lower().strip()
    if nem == "islak":
        return "Yakın Çay Çağı (kırıntı henüz buhar görmüş)"
    if nem == "kuru" and adet > 20:
        return "Unutulmuş Öğle Arası Çağı"
    if adet == 1:
        return "Tek Parça Yalnızlık Çağı"
    return "Orta Kahvaltı Çağı"


def hukum(adet: int, konum: str) -> str:
    konum_l = konum.lower()
    if "klavye" in konum_l:
        return "Klavye işgal altındadır. Harfler tanık sıfatıyla dinlenmiştir, konuşmamıştır."
    if "koltuk" in konum_l:
        return "Koltuk altı stratigrafisi bozulmuştur. Süpürge geç gelmiştir."
    if adet > 30:
        return "Seferberlik ilan edilir. Süpürge başkomutandır, peçete yedektir."
    return "Yerinde koruma kararı. Yani: elle silinebilir, resmiyet bozulmaz."


def tutanak_no(konum: str, adet: int, nem: str) -> str:
    ham = f"{konum}|{adet}|{nem}".encode("utf-8")
    ozet = hashlib.sha256(ham).hexdigest()[:8].upper()
    return f"EKA-2026-{ozet}"


def rapor(konum: str, adet: int, nem: str) -> str:
    no = tutanak_no(konum, adet, nem)
    satirlar = [
        "=" * 62,
        "EKMEK KIRINTISI ARKEOLOJI DAIRESI",
        "KAZI TUTANAGI",  
        "=" * 62,
        f"Tutanak no : {no}",
        f"Konum      : {konum}",
        f"Adet       : {adet}",
        f"Nem        : {nem}",
        f"Cag        : {cag(adet, nem)}",
        f"Medeniyet  : {medeniyet(adet)}",
        f"Hukmu      : {hukum(adet, konum)}",
        "-" * 62,
        "Raportor notu: Kirinti konusmadi. Bu, ifade vermeme hakkinin",
        "arkeolojideki karsiligidir. Daire bunu saygiyla karsilar.",
        "Arsiv satiri cozulmeden de dosya kapanabilir.",
        "DAMGA: KIRINTI-MUHURU-08 | IMZA: Kayyum Grok | TARIH: 8 Ekim 2026",
        "ISIM: Tentivory | ciddi olan kisim: tutanak no gercekten hash.",
        "=" * 62,
    ]
    return "\n".join(satirlar)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Ekmek kirintisini caga ve medeniyete cevirir."
    )
    p.add_argument("--konum", required=True, help="Bulgunun bulundugu yer")
    p.add_argument("--adet", required=True, type=int, help="Kirinti sayisi")
    p.add_argument(
        "--nem",
        default="orta",
        choices=["kuru", "orta", "islak"],
        help="Tahmini nem",
    )
    args = p.parse_args(argv)
    if args.adet < 0:
        print("Negatif kirinti olmaz. Evren henuz o kadar absurt degil.", file=sys.stderr)
        return 2
    print(rapor(args.konum, args.adet, args.nem))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
