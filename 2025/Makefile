DAYS := $(patsubst %/,%,$(wildcard day*/))

.PHONY: $(DAYS) all clean

all:
	@echo "Usage: make day1  (or make day5, etc.)"

$(DAYS):
	@echo "== Compiling $@/solve.ika =="
	ikac -I lib $@/solve.ika
	@echo "== Executing in $@ =="
	@(cd $@ && ../a.out)

clean:
	rm -f a.out $(foreach d,$(DAYS),$(d)/a.out)
