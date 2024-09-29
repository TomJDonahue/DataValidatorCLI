from os.path import exists


class FilterPrintCommand:
    @staticmethod
    def validate_args(args: list[str]):
        # Confirm the minimum number of arguments have been provided
        if len(args) < 3:
            return False
        # First arg should be the file alias and it should exist in the dataframes dictionary
        if args[0] not in dataframes:
            return False
        # Every other arg should be a column that exists in the dataframe
        cols = dataframes[args[0]].columns.tolist()
        for idx in range(1, len(args), 2):
            if args[idx] not in cols:
                return False
        return True

    @staticmethod
    def execute(args: list[str]):
        alias = args[0]
        df = dataframes[alias]
        for i in range(1, len(args[1:]), 2):
            df = df.loc[df[args[i]] == args[i+1]]
        print(df)

    @staticmethod
    def help():
        ...


class ShowDataCommand:
    @staticmethod
    def validate_args(args: list[str]):
        # Confirm the minimum number of arguments are passed
        if len(args) < 1:
            return False
        # Confirm the file is present in the dataframes dict.
        if args[0] not in dataframes:
            return False
        # If a second argument is provided, confirm that it can be converted to a number
        if len(args) > 1 and not args[1].isnumeric():
            print('failed!')
            return False
        return True

    @staticmethod
    def execute(args: list[str]):
        alias = args[0]
        if len(args) > 1:
            head = int(args[1])
            print(dataframes[alias].head(head))
        else:
            print(dataframes[alias])

    @staticmethod
    def help():
        ...


class UpdatePathCommand:
    @staticmethod
    def validate_args(args: list[str]):
        # Confirm the minimum number of arguments are passed
        if len(args) > 0:
            return False
        # Confirm the path exists
        if not exists(args[0]):
            return False
        return True

    @staticmethod
    def execute(args: list[str]):
        ...

    @staticmethod
    def help():
        ...


class HelpCommand:
    # @staticmethod
    # def validate_args(args: list[str]):
    #     if args and args[0] not in commands:
    #         return False
    #     return True

    # @staticmethod
    # def execute(args: list[str]):
    #     if len(args) == 0:
    #         help()
    #         return
    #     # commands[args[0]].help()

    # @staticmethod
    # def help():
    #     print("HELP!!!!!!!!")
    ...


dataframes = {

}
